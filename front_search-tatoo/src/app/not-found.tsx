import Link from "next/link";

export default function NotFound() {
    return (
      <div className="flex flex-col items-center justify-center">
        <h1 className="text-center font-bold mt-9 text-5xl">
          Error 404 - Página não encontrada!
        </h1>

        <p className="text-center font-bold text-4xl mt-3">Essa página não existe</p>

        <p className="text-center font-bold mt-7">Páginas do app:
            <ul className="mt-3">
                <li>
                    <Link href="/">
                    👉 Resgistrar tatuador
                    </Link>
                </li>
                <li>
                    <Link href="/search">
                    👉 Buscar tatuador
                    </Link>
                </li>
            </ul>
        </p>
      </div>
    )
  }