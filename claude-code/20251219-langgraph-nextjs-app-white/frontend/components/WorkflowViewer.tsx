'use client';

import { useState, useEffect } from 'react';

interface AgentInfo {
  name: string;
  description: string;
  order: number;
}

interface WorkflowInfo {
  agents: AgentInfo[];
  description: string;
}

export default function WorkflowViewer() {
  const [isExpanded, setIsExpanded] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [workflowInfo, setWorkflowInfo] = useState<WorkflowInfo | null>(null);

  // Fetch workflow info when component mounts
  useEffect(() => {
    const fetchWorkflowInfo = async () => {
      try {
        const response = await fetch('http://localhost:8002/api/workflow/info');
        if (!response.ok) {
          throw new Error('Failed to fetch workflow info');
        }
        const data = await response.json();
        setWorkflowInfo(data);
      } catch (err) {
        console.error('Error fetching workflow info:', err);
      }
    };

    fetchWorkflowInfo();
  }, []);

  const handleToggle = () => {
    setIsExpanded(!isExpanded);
    if (!isExpanded) {
      setIsLoading(true);
      setError(null);
    }
  };

  const handleImageLoad = () => {
    setIsLoading(false);
  };

  const handleImageError = () => {
    setIsLoading(false);
    setError('ワークフローの読み込みに失敗しました');
  };

  return (
    <div className="bg-white border border-slate-200 rounded-xl overflow-hidden shadow-md">
      {/* Header */}
      <button
        onClick={handleToggle}
        className="w-full p-6 bg-gradient-to-r from-blue-50 to-indigo-50 hover:from-blue-100 hover:to-indigo-100 text-left flex items-center justify-between transition-all duration-200"
      >
        <div>
          <h2 className="text-xl font-bold text-slate-900">
            ワークフロー設計
          </h2>
          <p className="text-sm text-slate-600 mt-1">
            LangGraphによるマルチエージェントワークフローの可視化
          </p>
        </div>
        <svg
          className={`w-6 h-6 text-slate-600 transform transition-transform duration-200 ${
            isExpanded ? 'rotate-180' : ''
          }`}
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M19 9l-7 7-7-7"
          />
        </svg>
      </button>

      {/* Content */}
      {isExpanded && (
        <div className="p-6 bg-slate-50/30">
          {isLoading && (
            <div className="flex justify-center items-center h-64">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
            </div>
          )}

          {error && (
            <div className="flex justify-center items-center h-64">
              <div className="text-red-600 text-center">
                <svg
                  className="w-12 h-12 mx-auto mb-4"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
                <p className="font-medium">{error}</p>
              </div>
            </div>
          )}

          <div className={isLoading || error ? 'hidden' : 'flex justify-center'}>
            <img
              src={`http://localhost:8002/api/workflow/graph?t=${Date.now()}`}
              alt="LangGraph Workflow Visualization"
              className="max-w-full h-auto border border-slate-200 rounded-lg shadow-sm bg-white"
              onLoad={handleImageLoad}
              onError={handleImageError}
            />
          </div>

          {workflowInfo && (
            <div className="mt-6 p-5 bg-gradient-to-br from-blue-50 to-indigo-50 rounded-xl border border-blue-100 shadow-sm">
              <h3 className="font-bold text-slate-900 mb-2">
                エージェント構成:
              </h3>
              <p className="text-sm text-slate-600 mb-4">
                {workflowInfo.description}
              </p>
              <ul className="space-y-2.5 text-sm text-slate-700">
                {workflowInfo.agents.map((agent) => (
                  <li key={agent.name} className="flex items-start">
                    <span className="font-bold mr-2 text-blue-700">
                      {agent.order}. {agent.name}:
                    </span>
                    <span>{agent.description}</span>
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      )}
    </div>
  );
}
