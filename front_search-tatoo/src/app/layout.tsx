import "./globals.css";

import { Header } from "../components/header";
import { Metadata } from "next";

export const metadata: Metadata = {
  title: "Consumo de API e indexição reversa",
  description: "Consumo de API e indexição reversa",
}


export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`antialiased`}
        cz-shortcut-listen="true"
      >
        <Header />
        {children}
      </body>
    </html>
  );
}
