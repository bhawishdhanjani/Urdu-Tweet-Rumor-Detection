import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import { Providers } from "./provider";
import Background from "../components/Background";
import { Navbar } from "@/components/Navbar";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Rumor or Fact Checker",
  description:
    "This applicaatiohn will help you identify where tweet written realy is a fact or a rummor",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={"dark text-foreground bg-background" + inter.className}>
        <Background />
        <Navbar />
        <div>
          <Providers>{children}</Providers>
        </div>
      </body>
    </html>
  );
}
