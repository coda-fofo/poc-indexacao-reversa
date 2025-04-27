buscador_front -> buscador_service "Realiza busca de tatuadores"
buscador_front -> indexador_service "Cadastrar novos tatuadores"

buscador_service -> tokenizador_core "Tokenizar a busca realizada pelo usuário"
buscador_service -> motor_busca_db "Busca por tatuadores através dos tokens"

indexador_service -> tokenizador_core "Tokenizar as principais informações do tatuador para adicionar no índice"
indexador_service -> motor_busca_db "Persiste os tatuadores e indexação"