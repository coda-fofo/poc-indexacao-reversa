const tatoo = {
  name: String,
  usuario: String,
  descricao: String
}


export default function register() {
  return (
    <div>
      <h1>
        Tela de registro
      </h1>

    <div className="flex items-center justify-center mt-10">
      <h2>Nome</h2>
      <input type="text" className="flex ml-2 border"/>
    </div>

    <div className="flex items-center justify-center mt-10">
      <h2>Usuario</h2>
      <input type="text" className="flex ml-2 border"/>
    </div>

    <div className="flex items-center justify-center mt-10">
      <h2>Descrição</h2>
      <input type="text" className="flex ml-2 border"/>
    </div>

    <div className="flex items-center justify-center mt-10">
      <button 
      type="submit" 
      className="p-3 px-6 bg-blue-500 text-white font-bold rounded-lg shadow hover:bg-blue-600 transition"
      >
        Gravar
      </button>
    </div>





    </div>
  )
}