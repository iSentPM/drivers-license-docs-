import { useEffect, useState } from 'react';

export const DataLensReport: React.FC = () => {
    const [token, setToken] = useState<string | null>(null);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchToken = async () => {
            try {
                const response = await fetch('http://localhost:8002/api/token');
                if (!response.ok) {
                    throw new Error('Ошибка при получении токена');
                }
                const data = await response.json();
                setToken(data.token);
            } catch (err) {
                setError(err instanceof Error ? err.message : 'Произошла ошибка при загрузке отчета');
            }
        };

        fetchToken();
    }, []);

    if (error) {
        return (
            <div style={{ color: 'red', padding: '20px' }}>
                Ошибка: {error}
            </div>
        );
    }

    if (!token) {
        return (
            <div style={{ padding: '20px' }}>
                Загрузка отчета...
            </div>
        );
    }

    return (
        <div style={{ 
            width: '100%', 
            height: '100%',
            flex: 1,
            display: 'flex'
        }}>
            <iframe
                src={`https://datalens.yandex.cloud/embeds/dash#dl_embed_token=${token}`}
                width="100%"
                height="100%"
                frameBorder="0"
                title="DataLens Report"
                style={{ 
                    border: 'none',
                    width: '100%',
                    height: '100%',
                    display: 'block',
                    flex: 1
                }}
            />
        </div>
    );
}; 