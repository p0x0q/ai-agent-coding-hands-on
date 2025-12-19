import ChatInterface from "../components/ChatInterface";
import WorkflowViewer from "../components/WorkflowViewer";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-6 gap-8">
      <div className="w-full max-w-4xl">
        <h1 className="text-4xl font-bold text-center mb-10 bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
          AI Multi-Agent Chat
        </h1>
        <ChatInterface />
      </div>

      <div className="w-full max-w-4xl">
        <WorkflowViewer />
      </div>
    </main>
  );
}
