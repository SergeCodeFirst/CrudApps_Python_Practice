import { useEffect, useState } from "react";

import axios from 'axios';

const Home = (props) => {
    const [greet, setGreet] = useState({});

    useEffect(() => {
        axios.get("http://localhost:5001/api")
            .then(res => {
                console.log(res.data);
                setGreet(res.data)
            })
            .catch(err => {
                console.log({error: err, msg:"Can not get the greetings"});
            })
    }, []);
    return <div>
        <h1>Hello from home 1</h1>
        <h2>{greet.home}</h2>
    </div>
}

export default Home