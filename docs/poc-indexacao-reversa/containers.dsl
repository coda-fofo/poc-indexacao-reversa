group "PoC Indexação Reversa" {
    motor_busca = softwareSystem "Motor de Busca" "Demonstração de um sistema para buscas usando indexação reversa" {
        buscador_front = Container "buscador-front" "Frontend para buscar e registrar tatuadores" "React" "NextJS" {
            tags "NextJS"
        }
        
        indexador_service = Container "indexador-service" "Serviço para a criação e indexação de tatuadores no banco de dados" "Python" "FastAPI" {
            tags "FastAPI"
        }

        buscador_service = Container "buscador-service" "Serviço para buscar por tatuadores" "Python" "FastAPI" {
            tags "FastAPI"
        }


        tokenizador_core = Container "tokenizador-core" "Serviço para a tokenização de linguagem natural" "Python" "FastAPI" {
            tags "FastAPI"
        }

        motor_busca_db = Container "motorbuscadb" "Banco de dados para armazenamento dos tatuadores e do índice" "Postgres" "Postgres" {
            tags "Postgres"
        }
    }
}