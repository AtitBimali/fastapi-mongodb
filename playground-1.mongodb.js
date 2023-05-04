/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

const database = 'Cluster0';
const collection = 'Task';

// The current database to use.
use(database);

// Create a new collection with the specified schema.
db.createCollection(collection, {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      required: ['title'],
      properties: {
        id: {
          bsonType: 'objectId',
          description: 'The unique identifier for the task'
        },
        title: {
          bsonType: 'string',
          description: 'The title of the task'
        },
        description: {
          bsonType: 'string',
          description: 'The description of the task'
        },
        completed: {
          bsonType: 'bool',
          description: 'Whether the task is completed or not'
        },
        created_at: {
          bsonType: 'date',
          description: 'The creation date of the task'
        },
        updated_at: {
          bsonType: 'date',
          description: 'The date of the task when it was updated'
        }
      }
    }
  }
});