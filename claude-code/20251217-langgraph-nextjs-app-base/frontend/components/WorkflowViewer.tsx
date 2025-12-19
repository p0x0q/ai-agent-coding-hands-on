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
    <div className="border border-gray-300 rounded-lg overflow-hidden">
      {/* Header */}
      <button
        onClick={handleToggle}
        className="w-full p-4 bg-gray-100 hover:bg-gray-200 text-left flex items-center justify-between transition-colors"
      >
        <div>
          <h2 className="text-xl font-semibold text-gray-900">
            ワークフロー設計
          </h2>
          <p className="text-sm text-gray-600 mt-1">
            LangGraphによるマルチエージェントワークフローの可視化
          </p>
        </div>
        <svg
          className={`w-6 h-6 text-gray-600 transform transition-transform ${
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
        <div className="p-6 bg-white">
          {isLoading && (
            <div className="flex justify-center items-center h-64">
              <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
            </div>
          )}

          {error && (
            <div className="flex justify-center items-center h-64">
              <div className="text-red-500 text-center">
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
                <p>{error}</p>
              </div>
            </div>
          )}

          <div className={isLoading || error ? 'hidden' : 'flex justify-center'}>
            <img
              src={`http://localhost:8002/api/workflow/graph?t=${Date.now()}`}
              alt="LangGraph Workflow Visualization"
              className="max-w-full h-auto border border-gray-200 rounded-lg shadow-sm"
              onLoad={handleImageLoad}
              onError={handleImageError}
            />
          </div>

          {workflowInfo && (
            <div className="mt-4 p-4 bg-blue-50 rounded-lg">
              <h3 className="font-semibold text-gray-900 mb-2">
                エージェント構成:
              </h3>
              <p className="text-sm text-gray-600 mb-3">
                {workflowInfo.description}
              </p>
              <ul className="space-y-2 text-sm text-gray-700">
                {workflowInfo.agents.map((agent) => (
                  <li key={agent.name} className="flex items-start">
                    <span className="font-semibold mr-2">
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
