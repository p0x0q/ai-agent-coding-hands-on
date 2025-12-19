import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'AI Multi-Agent Chat',
  description: 'LangGraph powered multi-agent chat application',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="ja">
      <body className="antialiased">{children}</body>
    </html>
  );
}
