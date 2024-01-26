export function getTournamentLog() {
    fetch('/tournamnet/log', {
        method: 'GET',
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        });
}

export function postTournamentLog() {
    const num = 10; // 이 부분은 필요에 따라 수정하세요.

    fetch('/tournamnet/log', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ num: num }),
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch((error) => {
            console.error('Error:', error);
        });
}
