'use client'

import { useState } from "react"
import { ListTatoo } from "@/components/searchComponents/listTatoo"

export default function search() {
    const [query, setQuery] = useState("")
    const [response, setResponse] = useState<any[]>([])

    const handleSearch = async () => {
        
        const res = await fetch(`https://dummyjson.com/users/search?q=${query}`)
        const data = await res.json()

        console.log(data.users)

        setResponse(data.users)
        

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