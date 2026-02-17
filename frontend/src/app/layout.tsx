import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "MMAM — Intelligence Core",
  description: "Murillo Medina Asset Management: AI-powered terminal with NVIDIA NIM, real-time analytics, and automated trading.",
};

import ChatWidget from "@/components/ai/ChatWidget";
import { PortfolioProvider } from "@/context/PortfolioContext";

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased bg-background text-foreground`}
      >
        <PortfolioProvider>
          {children}
          <ChatWidget />
        </PortfolioProvider>
      </body>
    </html>
  );
}
