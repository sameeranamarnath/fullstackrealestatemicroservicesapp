
An event-driven real estate web application with a house collection. With this application, users  and prospective buyers can browse the properties in the collection to see if they like any of them.

Frontend stack= React TypeScript, HTML, CSS, and Bootstrap. 
Backend stack
a) config ( django,mysql,docker)
b) houses ( django,mysql,docker)
c) core ( flask,mysql,docker)
The communication channel between the microservices is RabbitMQ, which will serve as the message broker and the event bus. 
Micro-apps structure:

a)The Config app will configure all the installed apps, middleware, URLs/endpoints, and databases for the back-end service. 

b) The Houses app will contain house creation, listing, updating, and deletion.

c) The Core app will have house liking, checking, and other actions. 

The Config app will oversee the Houses app internally, while the Core app will make internal API requests to the Config and Houses apps.
