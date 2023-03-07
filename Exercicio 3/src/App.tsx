import { Board } from "./components/Board/Board"
import { useState } from "react";
import { SquareValue } from "./components/Square/Square";
import './global.css'

function calculateWinner(squares: SquareValue[]): SquareValue {
  const lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ];
  for (let i = 0; i < lines.length; i++) {
    const [a, b, c] = lines[i];
    if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
      return squares[a];
    }
  }
  return null;
}


const App = () => {
  const [history, setHistory] = useState(Array<SquareValue>(9).fill(null));
  const [xIsNext, setXIsNext] = useState(true);

  function handleClick(i: number) {
    const squares = [...history];
    if (calculateWinner(squares)) {
      return;
    }
    squares[i] = xIsNext ? 'X' : 'O';
    setHistory(squares);
    setXIsNext(!xIsNext);
  }

  return (
    <div className="App">
      <h1>Jogo da Velha</h1>
      <Board onClick={handleClick} squares={history}/>
    </div>
  )
}


export default App