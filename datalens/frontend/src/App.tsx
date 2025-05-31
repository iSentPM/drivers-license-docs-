import './App.css';
import { DataLensReport } from './components/DataLensReport';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Отчет DataLens</h1>
      </header>
      <main style={{ 
        flex: 1,
        height: 'calc(100vh - 100px)', // вычитаем высоту header
        padding: 0,
        overflow: 'hidden'
      }}>
        <DataLensReport />
      </main>
    </div>
  );
}

export default App; 