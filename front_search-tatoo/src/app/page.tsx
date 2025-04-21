"use client"

import { useState } from "react"

export default function register() {

  const [tatoo, setTatoo] = useState({
    nome: "",
    usuario: "",
    descricao: ""
  })

  const sendData = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    try {
      const res = fetch('http://127.0.0.1:3000/gravar', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          nome: tatoo.nome,
          usuario: tatoo.usuario,
          descricao: tatoo.descricao
        })
      });
      
      const data = (await res).json()
      console.log("Usuario cadastrado com sucesso:", data);
      console.log((await res).json)

      setTatoo({
        nome: "",
        usuario: "",
        descricao: ""
      });

      } catch(error) {
        console.error("Erro ao cadastrar:", error);
      } 
  }
      

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { id, value } = e.target;
    setTatoo(prev => ({ ...prev, [id]: value }));
  }

  return (
    <form
      className="w-full max-w-md mx-auto mt-10"
      onSubmit={sendData}
    >

      <div className="relative w-full max-w-md mt-6">
        <label
          htmlFor="nome"
          className="absolute -top-2 left-4 bg-white px-1 text-sm text-gray-600"
        >
          Nome
        </label>
        <input
          id="nome"
          type="text"
          className="w-full border border-gray-300 rounded-md px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          value={tatoo.nome}
          onChange={handleChange}
        />
      </div>

      <div className="relative w-full max-w-md mt-6">
        <label
          htmlFor="nome"
          className="absolute -top-2 left-4 bg-white px-1 text-sm text-gray-600"
        >
          Usuario
        </label>
        <input
          id="usuario"
          type="text"
          className="w-full border border-gray-300 rounded-md px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          value={tatoo.usuario}
          onChange={handleChange}
        />
      </div>

      <div className="relative w-full max-w-md mt-6">
        <label
          htmlFor="nome"
          className="absolute -top-2 left-4 bg-white px-1 text-sm text-gray-600"
        >
          Descrição
        </label>
        <input
          id="descricao"
          type="text"
          className="w-full border border-gray-300 rounded-md px-4 py-3 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
          value={tatoo.descricao}
          onChange={handleChange}
        />
      </div>

      <div className="relative w-full max-w-md mt-6 ">
        <button
          type="submit"
          className="p-3 px-6 bg-blue-500 text-white font-bold rounded-lg shadow hover:bg-blue-600 transition w-full"

        >
          Gravar
        </button>
      </div>

    </form>
  )
}