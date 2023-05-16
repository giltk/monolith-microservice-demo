import {useState, useCallback} from 'react';


function App() {
  const [data, setData] = useState([{}]);
  const sendRequest = useCallback(async () => {
    // send the actual request
    fetch('/api/users').then(
          res => res.json()
        ).then(
          data => setData(data)
        )
  }, [])

  return (
    <div>
      <h1>User list:</h1>
      {(typeof data.users === 'undefined') ? (
        <input type="button" onClick={sendRequest} value='Get user list'/>
    ) : (
        data.users.map((user, i) => (
          <p key={i}>{user}</p>
        ))
      )}
    </div>
  );
}

export default App;
