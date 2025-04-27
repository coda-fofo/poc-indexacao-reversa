import { Tatoo } from "@/app/dtos/tatoo";

export function ListTatoo({ response }: { response: Tatoo[] }) {
    return (
        <div>
            <div className="flex items-center justify-center mt-10">
                <div className="w-[746px] mx-auto mt-4 bg-gray-100 rounded shadow-md">
                        { response.length === 0 ? ( 
                            <p className="font-bold text-center p-4">Nenhum usuario encontrado</p>

                        ): (response.map(tatoo => ( 
                            <ul key={tatoo.id} className="p-4 rounded">
                                <li>
                                    <h2 className="font-bold">
                                        {tatoo.nome_de_exibicao}
                                    </h2>
                                    <p>@{tatoo.nome_de_usuario}</p>
                                    <p>Descrição: {tatoo.descricao}</p>

                                     {tatoo.hashtags && tatoo.hashtags.length > 0 && (

                                            <div className="mt-2 flex flex-wrap gap-2">
                                                {tatoo.hashtags.map((tag: string, index: number) => (
                                                    <span 
                                                    key={index}
                                                    className="bg-blue-600 text-amber-50 px-3 py-1 text-sm rounded-full">
                                                        #{tag}
                                                    </span> 
                                                ))}
                                            </div>
                                        )
                                    }
                                    
                                    <hr className="text-gray-200 mt-5" />
                                </li>
                            </ul>
                        )))} 
                </div>
            </div>
        </div>
    )
}