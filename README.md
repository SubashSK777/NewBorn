```mermaid
flowchart TD
    A([Start]) --> B{Create Payload}
    B --> C[Embed Payload in HTTPS Request]
    C --> D{Bypass Firewall?}
    D -->|Yes| E[Send Request to Server]
    D -->|No| F[Try Different Payload]
    E --> G{Analyze Response Time}
    G -->|Vulnerable| H[Identified Vulnerability]
    G -->|Not Vulnerable| I[No Vulnerability]
    F --> G
    H --> J([End])
    %% Styles for black-and-white theme
    style A fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style B fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style C fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style D fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style E fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style F fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style G fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style H fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style I fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
    style J fill:#ffffff,stroke:#000000,stroke-width:2px,color:#000000
