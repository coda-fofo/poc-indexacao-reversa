'use client'

export function ListTatoo({ response }: { response: any[] }) {

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
                                        {tatoo.firstName} {tatoo.lastName}
                                    </h2>
                                    <p>@{tatoo.username}</p>
                                    <p>Email: {tatoo.email}</p>
                                    <hr className="text-gray-200 mt-5" />
                                </li>
                            </ul>
                        )))} 
                </div>
            </div>
        </div>
    )
}