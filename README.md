# FastAPI Application

This is a FastAPI application that provides endpoints for managing users, events, and registrations.

## API Endpoints

### User

#### Signup User

- **Method**: `POST`
- **Endpoint**: `/users/signup`
- **Description**: Signup a new user.

#### Verify User

- **Method**: `POST`
- **Endpoint**: `/users/signup/verify`
- **Description**: Verify user registration.

#### Login User

- **Method**: `GET`
- **Endpoint**: `/users/login`
- **Description**: Login user.

#### Delete User

- **Method**: `DELETE`
- **Endpoint**: `/users/delete`
- **Description**: Delete user.

#### Verify Delete User

- **Method**: `DELETE`
- **Endpoint**: `/users/delete/verify`
- **Description**: Verify user deletion.

### Event

#### Create Event

- **Method**: `POST`
- **Endpoint**: `/events/create`
- **Description**: Create a new event.

#### Update Event

- **Method**: `PUT`
- **Endpoint**: `/events/update`
- **Description**: Update event details.

#### Delete Event

- **Method**: `DELETE`
- **Endpoint**: `/events/delete`
- **Description**: Delete event.

#### Get Event

- **Method**: `GET`
- **Endpoint**: `/events/get`
- **Description**: Get event details.

#### Get All Events

- **Method**: `GET`
- **Endpoint**: `/events/get/all`
- **Description**: Get details of all events.

### Registration

#### Register Event

- **Method**: `POST`
- **Endpoint**: `/events/register`
- **Description**: Register for an event.

#### Get Registered Events

- **Method**: `GET`
- **Endpoint**: `/events/get/registered`
- **Description**: Get events for which the user is registered.

#### Get Registered Events (Conditional)

- **Method**: `GET`
- **Endpoint**: `/events/get/registered/conditional`
- **Description**: Get registered events based on conditions.

#### Checkin User

- **Method**: `PUT`
- **Endpoint**: `/events/users/checkin`
- **Description**: Checkin a user for an event.

#### Get All Users

- **Method**: `GET`
- **Endpoint**: `/events/users/download`
- **Description**: Download details of all users.

### Default

#### Root

- **Method**: `GET`
- **Endpoint**: `/`
- **Description**: Root endpoint.

## How to Run

1. Install dependencies: `pip install -r requirements.txt`
2. Run the FastAPI application: `uvicorn main:app --reload`
3. Access the API at `http://127.0.0.1:8000`
