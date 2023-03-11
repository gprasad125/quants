# API Interaction

> Great fun…
> 

---

If your app has anything dynamic that requires data, chances are you will have to get it from an API. While there are multiple methods for sending data between the frontend and backend, this doc will focus mainly on HTTP.

---

# Fetch vs. Axios

Sending http requests and handling responses is usually done with the `Fetch` API ([link](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)) that JS supports natively or with the `Axios` library ([link](https://axios-http.com/)). `Fetch` is more basic. `Axios` comes with more features and quality of life (such as erroring on non-2xx status codes), though you do add slightly more JS to your app bundle (~11kb gzipped). Using either is probably fine unless your target user has 1 bar of signal. 

If you want to use `Fetch` though, you might want to create your own wrapper for it that throws errors if the response status code is not 2xx, since `Fetch` doesn’t error for bad status codes for some reason. Something like:

```jsx
async function modifiedFetch(url, options) {
		const res = await fetch(url, options);
		const json = await res.json();
		// check if response status code is 2xx.
		// if it's not ok, throw json.
		// fetch does not error for bad status codes like 400. 
		// don't ask why. I don't know why either.
		if (!res.ok) {
				throw { request: res };
		}
		// return result if status is 2xx.
		return json;
}

// then you can use just as normal
modifiedFetch('url', someOptions).then(data => {
		// do something with result
		console.log(data);
}).catch(err => {
		// do something with error
		if (err.request) {
				// status code was bad
		} else {
				// request failed to communicate with API
		}
});

// supports await
const data = await modifiedFetch('url', someOptions);
```

# Basic Requests

If you only require normal API interaction or want to minimize the app’s JS, then using normal React methods is fine. For example:

```jsx
function SomeComponent() {
		// track loading state
		const [loading, setLoading] = useState(true);
		// store API result
		const [data, setData] = useState();
		
		// run on component mount
		useEffect(() => {
				const url = 'some-url';
				const options = {
						method: 'GET'
				};
				// using native Fetch API for requests
				fetch(url, options).then(res => {
						// res.json() is asynchronous
						// need to wait for it to resolve
						return res.json();
				}).then(jsonData => {
						setData(jsonData);
						// update loading state
						setLoading(false);
				}).catch(err => {
						// handle any errors
				});
		}, []);
		
		if (loading) {
				// display a loading indicator
				return <h1>Loading...</h1>;
		}

		return (
				// display result
				<h1>{data}</h1>
		);
}
export default SomeComponent;
```

# Advanced Requests

If your app makes many API calls and would benefit from advanced features such as results caching, then using a library to handle that for you could be very helpful. They generally follow the same pattern for syntactical sugar:

```jsx
const asyncDataFetcher = async () => {
		const url = 'some-url';
		const options = {
				method: 'GET'
		};
		const res = await fetch(url, options);
		const json = await res.json();
		return json;
};

function SomeComponent() {
		const { data, loading, error } = someQueryCreator('some-key-for-caching', asyncDataFetcher);
		if (error) {
				return <ErrorHandling />;
		} else if (loading) {
				return <LoadingIndicator />;
		}
		
		return (
				// the component content
				<h1>{data}</h1>
		);
}
export default SomeComponent;
```

Besides handling the request for you, they also supply some advanced features like caching the results to prevent unnecessary refetches, automatic retries on request failure, and stuff like opportunistic updates. 

They are somewhat complicated and require some getting used to, but once you know how to use them they can become a powerful data handling layer for your app. 

Below are two popular options. For your purposes, there likely will not be much of an advantage of picking one over the other, so just go with whatever looks nicer/easier to learn.

### TanStack Query (previously named as useQuery)

> [https://tanstack.com/query/latest](https://tanstack.com/query/latest)
> 

### SWR

> [https://swr.vercel.app/](https://swr.vercel.app/)
>