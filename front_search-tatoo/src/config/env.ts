type Env = {
    NEXT_PUBLIC_BUSCADOR_SERVICE_URL: string;
    NEXT_PUBLIC_INDEXADOR_SERVICE_URL: string;
}

export function getEnv(): Env {
    // talvez com zod fique mais elegante
    // https://zod.dev
    if (!process.env.NEXT_PUBLIC_BUSCADOR_SERVICE_URL || !process.env.NEXT_PUBLIC_INDEXADOR_SERVICE_URL) {
        throw new Error('Env inválido. Verifique o arquivo .env');
    }
    
    return {
        NEXT_PUBLIC_BUSCADOR_SERVICE_URL: process.env.NEXT_PUBLIC_BUSCADOR_SERVICE_URL,
        NEXT_PUBLIC_INDEXADOR_SERVICE_URL: process.env.NEXT_PUBLIC_INDEXADOR_SERVICE_URL,
    }
}