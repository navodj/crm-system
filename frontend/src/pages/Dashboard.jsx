import { useEffect, useState } from "react";
import API from "../api/api";

export default function Dashboard() {
    const [data, setData] = useState(null);

    const fetchDashboard = async () => {
        const res = await API.get("/dashboard");
        setData(res.data);
    };

    useEffect(() => {
        fetchDashboard();
    }, []);

    if (!data) return <p>Loading...</p>;

    return (
        <div>
            <h2>Dashboard</h2>

            <p>Total Leads: {data.total_leads}</p>
            <p>New Leads: {data.new_leads}</p>
            <p>Qualified: {data.qualified_leads}</p>
            <p>Won: {data.won_leads}</p>
            <p>Lost: {data.lost_leads}</p>
            <p>Total Value: {data.total_value}</p>
            <p>Won Value: {data.won_value}</p>
        </div>
    );
}