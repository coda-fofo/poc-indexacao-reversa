'use client'

import { useState } from "react"
import { ListTatoo } from "@/components/searchComponents/listTatoo"
import { Tatoo } from "../dtos/tatoo"
import { getEnv } from "@/config/env"
import urlJoin from "url-join"

async function fazerBusca(query: string): Promise<Tatoo[]> {
    const env = getEnv();
    const params = new URLSearchParams({ 'pesquisa': query });
    const url = urlJoin(env.NEXT_PUBLIC_BUSCADOR_SERVICE_URL, 'buscador/buscar') + '?' + params.toString(); 
    const res = await fetch(url);
    return await res.json();
}

export default function Search() {
    const [query, setQuery] = useState("")
    const [response, setResponse] = useState<Tatoo[]>([])

    const handleSearch = async () => {
        const data = await fazerBusca(query);
        setResponse(data);
    }

    const handleKeyDown = (e: React.KeyboardEvent<HTMLInputElement>) => {
        if(e.key === 'Enter') { handleSearch() }
    }

    return (
        <div>
            <div className="flex items-center justify-center mt-10 gap-2">
                <input 
                    type="text" 
                    value={query} 
                    onChange={e => setQuery(e.target.value)} 
                    onKeyDown={handleKeyDown}
                    className="w-[600px] p-3 border rounded shadow"
                    placeholder="Buscar tatuador..."
                    />
                    
                <button 
                onClick={handleSearch} 
                className="p-3 px-6 bg-blue-500 text-white font-bold rounded-lg shadow hover:bg-blue-600 transition">
                    Pesquisar
                </button>
                    
            </div>

            <ListTatoo response={ response } />
        </div>
    )
}