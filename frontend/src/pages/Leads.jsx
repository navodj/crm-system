import { useEffect, useState } from "react";
import API from "../api/api";

export default function Leads() {
    const [leads, setLeads] = useState([]);

    const fetchLeads = async () => {
        const res = await API.get("/leads");
        setLeads(res.data);
    };

    useEffect(() => {
        fetchLeads();
    }, []);

    return (
        <div>
            <h2>Leads</h2>

            <ul>
                {leads.map((lead) => (
                    <li key={lead.id}>
                        {lead.lead_name} - {lead.status}
                    </li>
                ))}
            </ul>
        </div>
    );
}