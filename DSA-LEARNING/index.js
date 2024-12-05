


  let board = [
    'X', null, 'O', 'x', null, 'O', 'X', null, 'X'
  ]
  board = Array(9).fill(null)
function second(board) {
    let openPositions = []
    for (let i = 0; i< board.length; i++) {
        if (board[i] === null) {
            openPositions.push(i)
        }
    }
    console.log(openPositions[Math.floor(Math.random() * openPositions.length)], 'this is the second style')
}
second(board)