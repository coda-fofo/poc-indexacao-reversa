import Link from "next/link";

export function Header() {
    return (
        <header className="flex px-2 py-4 bg-gray-900 text-white">
            <div className="flex items-center justify-between w-full mx-auto max-w-7xl">

                <div>Consumo de API e indexição reversa</div>

                <nav>
                    <ul className="flex items-center justify-center gap-7">

                        <li>
                            <Link href="/"> 
                                Registrar Tatuador
                            </Link>
                        </li>

                        <li>
                        <Link href="/search"> 
                                Buscar
                            </Link>
                        </li>
                        
                    </ul>
                </nav>
            
            </div>
        </header>
    )
}