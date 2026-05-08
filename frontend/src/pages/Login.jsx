import { useState } from "react";
import API from "../api/api";

export default function Login({ setIsAuthenticated }) {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleLogin = async () => {
        try {
            const res = await API.post("/auth/login", {
                email,
                password
            });

            // ✅ save token
            localStorage.setItem("token", res.data.access_token);

            setIsAuthenticated(true);
        } catch (err) {
            alert("Login failed");
        }
    };

    return (
        <div>
            <h2>Login</h2>

            <input
                placeholder="Email"
                onChange={(e) => setEmail(e.target.value)}
            />

            <input
                placeholder="Password"
                type="password"
                onChange={(e) => setPassword(e.target.value)}
            />

            <button onClick={handleLogin}>Login</button>
        </div>
    );
}
