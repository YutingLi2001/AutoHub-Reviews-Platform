/**
 * Main function that handles the retrieval of dealership data from a Cloudant database.
 * @param {Object} params - Parameters that dictate which data should be retrieved.
 * @returns {Promise} - A promise that resolves with the response object containing status code, headers, and body.
 */
function main(params) {
    // Start a new promise to handle asynchronous operations
    return new Promise(function (resolve, reject) {
      // Require the CloudantV1 class from the IBM Cloudant library
      const { CloudantV1 } = require("@ibm-cloud/cloudant");
      // Require the IamAuthenticator class from the IBM Cloud SDK Core library
      const { IamAuthenticator } = require("ibm-cloud-sdk-core");
  
      // Set up the IAM authenticator with an API key
      const authenticator = new IamAuthenticator({
        apikey: "",
      });
  
      // Initialize a new Cloudant client instance and pass the authenticator
      const cloudant = CloudantV1.newInstance({
        authenticator: authenticator,
      });
  
      // Set the service URL for the Cloudant instance to connect to the database
      cloudant.setServiceUrl("");
  
      // Check if 'st' parameter is present, which indicates a query for dealerships by state
      if (params.st) {
        // Perform a database search for documents where the 'st' field matches the 'st' parameter
        cloudant
          .postFind({ db: "dealerships", selector: { st: params.st } })
          .then((result) => {
            // Determine the HTTP status code based on if documents were found
            let code = result.result.docs.length == 0 ? 404 : 200;
            // Resolve the promise with the result, status code, headers, and body
            resolve({
              statusCode: code,
              headers: { "Content-Type": "application/json" },
              body: result.result.docs,
            });
          })
          .catch((err) => {
            // Reject the promise if there is an error during the database query
            reject(err);
          });
      // Check if 'dealerId' parameter is present, which indicates a query for a specific dealership
      } else if (params.dealerId) {
        // Parse the dealerId parameter to an integer since it is expected to be a number
        const id = parseInt(params.dealerId);
        // Perform a database search for documents where the 'id' field matches the 'dealerId' parameter
        cloudant
          .postFind({
            db: "dealerships",
            selector: {
              id: id,
            },
          })
          .then((result) => {
            // Determine the HTTP status code based on if documents were found
            let code = result.result.docs.length == 0 ? 404 : 200;
            // Resolve the promise with the result, status code, headers, and body
            resolve({
              statusCode: code,
              headers: { "Content-Type": "application/json" },
              body: result.result.docs,
            });
          })
          .catch((err) => {
            // Reject the promise if there is an error during the database query
            reject(err);
          });
      } else {
        // If no parameters are provided, retrieve all documents from the 'dealerships' database
        cloudant
          .postAllDocs({ db: "dealerships", includeDocs: true })
          .then((result) => {
            // Determine the HTTP status code based on if any documents were found
            let code = result.result.rows.length == 0 ? 404 : 200;
            // Resolve the promise with the result, status code, headers, and body
            resolve({
              statusCode: code,
              headers: { "Content-Type": "application/json" },
              body: result.result.rows.map(row => row.doc),
            });
          })
          .catch((err) => {
            // Reject the promise if there is an error during the database query
            reject(err);
          });
      }
    });
  }