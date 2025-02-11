document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("form-tag").addEventListener("submit", async function (event) {
        event.preventDefault();

        let formData = new FormData(this);

        let agentData = {
            "agent_name": formData.get("agent-name"),
            "phone": formData.get("agent-phone"),
            "email": formData.get("agent-email")
        };

        try {
            let response = await fetch("/api/resource/Agent", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "Authorization": "token YOUR_API_KEY:YOUR_API_SECRET"
                },
                body: JSON.stringify(agentData)
            });

            let agentResponse = await response.json();

            if (response.ok && formData.get("agent-image").size > 0) {
                let agentName = agentResponse.data.name;
                await uploadAgentImage(formData.get("agent-image"), agentName);
            }

            alert("Agent created successfully!");
            document.getElementById("form-tag").reset();
        } catch (error) {
            console.error("Error:", error);
            alert("Failed to create agent!");
        }
    });

    async function uploadAgentImage(file, agentName) {
        let formData = new FormData();
        formData.append("file", file);
        formData.append("is_private", 0);
        formData.append("doctype", "Agent");
        formData.append("docname", agentName);

        let response = await fetch("/api/method/upload_file", {
            method: "POST",
            headers: {
                "Authorization": "token 14322ca6b0c9534:52c5bebefb57e8d "
            },
            body: formData
        });

        if (!response.ok) {
            throw new Error("Image upload failed!");
        }
    }
});
