# Full_Stack_CS_350
Coursework for SNHU CS350 (MongoDB / Python/ Jupyter) 
### How do you write programs that are maintainable, readable, and adaptable?
When writing programs like the CRUD Python module for Project One, maintainability and readability are often my highest priorities. I place focus on the use ofclear class structures, role based method names (create, read, update, delete), and error handling to ensure that anyone (well mostly) reviewing the module would quickly understand its purpose. Each function was carefully scoped to a single responsibility, which made adapting the module for different database collections or authentication settings a relative breeze.

An important advantage of working this way was modularity: the CRUD module could be imported and reused directly in Project Two without needing to modify the original code. It created a clean separation of database access logic from the dashboard logic. In the future, this module could easily be adapted to work with other collections, other databases, or even extended to include new functionality like batch updates or aggregation queries without rewriting the entire dashboard.

### How do you approach a problem as a computer scientist?
When Grazioso Salvare outlined their dashboard requirements, I approached the problem by carefully identifying what was expected at each step. For the database, I first mapped how MongoDB stores animal records and verified that the filtering conditions (breed, age, sex) could be modeled with queries. For the dashboard, I visualized how users would need to interact with widgets like radio buttons, data tables, maps, and pie charts.

This project differed from previous assignments because I had to design a system that would not just "work once," but work across multiple types of user interactions, data views, and filtering scenarios. I spent more a lot of time upfront organizing code and testing iteratively after each feature was added. In the future, for other client requests, I would continue using techniques like modular Python classes, interactive dashboards, and clearly defined client-driven requirements to create solutions that are both functional and maintainable.

### What do computer scientists do, and why does it matter?
Computer scientists solve real-world problems by applying technical know how to create structured and efficient solutions. In projects like this one, the goal is not just to process data but to make data actionable, visual, and easy to interpret. My work on the Grazioso Salvare dashboard helps the company quickly find and evaluate dogs for their search-and-rescue training programs — something that would have taken far longer using static spreadsheets or manual searches.

By designing clean databases, flexible modules, and responsive dashboards, computer scientists give companies ready made tools to make better decisions, optimize their workflows, and extend their impact in the real world. 
