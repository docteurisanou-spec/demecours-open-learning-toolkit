# Architecture

The toolkit provides reusable education services that operate independently from the proprietary Dèmè-Cours Glide interface.

1. Versioned JSON learning content.
2. An assessment API that delivers questions and scores attempts.
3. Anonymous aggregate public metrics.
4. OpenAPI documentation at `/docs`.

Any standards-compliant client can use the HTTP API. Glide may remain one client, but is not required to run, test, modify or reuse the toolkit.

Prototype metrics currently reset on restart. A production milestone will add an open-source database adapter, privacy safeguards, authentication, monitoring and deployment automation.
