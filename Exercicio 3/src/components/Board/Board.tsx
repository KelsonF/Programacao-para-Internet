import './Board.css'
import { Square } from '../Square/Square'
import { SquareValue } from '../Square/Square';

interface BoardProps {
    squares: SquareValue[];
    onClick: (i: number) => void;
}

export const Board = (props: BoardProps) => {
    function renderSquare(i: number) {
        return (
            <Square
                value={props.squares[i]}
                onClick={() => props.onClick(i)}
            />
        );
    }

    return (
        <div className="board">
            {renderSquare(0)}
            {renderSquare(1)}
            {renderSquare(2)}
            {renderSquare(3)}
            {renderSquare(4)}
            {renderSquare(5)}
            {renderSquare(6)}
            {renderSquare(7)}
            {renderSquare(8)}
        </div>
    )
}
