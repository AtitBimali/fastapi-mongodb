/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

const database = 'Cluster0';
const collection = 'Task';

// The current database to use.
use(database);


// Update all documents in the Task collection to add a new field "updated_at"
db.getCollection(collection).updateMany(
  {},
  { $set: { updated_at: null } }
);