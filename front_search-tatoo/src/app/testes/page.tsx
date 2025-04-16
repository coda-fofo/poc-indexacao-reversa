'use client';

import { useEffect, useState } from "react";

export default function testes() {
    const [users, setUsers] = useState<any[]>([]);

    useEffect(() => {
        async function fetchUsers() {
            const response = await fetch('https://dummyjson.com/users?limit=5');
            const data = await response.json();

            setUsers(data.users)
        }

        fetchUsers();
    }, [])


    return (
        <div>
            {users.map(user => (
                <div key={user.id} className="p-4 border rounded">
                    <h2 className="font-bold">
                        Name: {user.firstName} {user.lastName}
                    </h2>
                    <p className="font-bold">Age: {user.age} </p>
                </div>
            ))}
        </div>
    )
  }