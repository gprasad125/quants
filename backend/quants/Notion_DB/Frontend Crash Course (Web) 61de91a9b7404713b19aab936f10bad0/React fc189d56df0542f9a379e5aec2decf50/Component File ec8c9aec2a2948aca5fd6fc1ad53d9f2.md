# Component File

> Keep things consistent
> 

---

# Overview

It’s a good idea to have a consistent organization within component files as well. In React, components are simply functions that return JSX. This gives us a few zones of separation already:

```jsx
// constants, generic functions/methods can go here

function SomeComponent() {
		// component logic and behavior goes here
		const [count, setCount] = useState(0);
		
		const incrementCount = () => {
				setCount(prev => prev + 1);
		};
		
		const countGreaterThanFive = count > 5;
		
		// everything below has to do with display
		return (
				<button onClick={incrementCount}>
						Count: {count}
				</button>
				{
						countGreaterThanFive ?
								<span>Count is > 5!</span>
						:
								null
				}
		);
}

export default SomeComponent;
```

# The Ternary Issue

Sometimes you might want to conditionally render an element only if a certain condition is true. One common method is to use a ternary operator in the render/return section. In the above example, this would be the `span` that indicates that `count` is more than five. For simple and small conditions and elements, this is fine. Otherwise it may become bulky and syntactically intricate. 

### Moving Logic Up

A more elegant solution might be to move the logic into the logic section (above the `return`) and resolve it using normal javascript logic:

```jsx

function SomeComponent() {
		// component logic and behavior goes here
		const [count, setCount] = useState(0);
		
		const incrementCount = () => {
				setCount(prev => prev + 1);
		};
		
		let countGreaterThanFive;
		if (count > 5) {
				countGreaterThanFive = (
						<span>Count is > 5!</span>
				);
		}
		
		// everything below has to do with display
		return (
				<button onClick={incrementCount}>
						Count: {count}
				</button>
				{countGreaterThanFiveText}
		);
}

export default SomeComponent;
```

### Component Abstraction

If the above still is unsatisfactory, an even cleaner solution would be to create a component to abstract it for you (stolen from [SolidJS](https://www.solidjs.com/) 🙃):

```jsx
function Show({ when, children }) {
		if (when) {
				return children;
		}
		return null;
}
```

```jsx
function SomeComponent() {
		// component logic and behavior goes here
		const [count, setCount] = useState(0);
		
		const incrementCount = () => {
				setCount(prev => prev + 1);
		};
		
		// everything below has to do with display
		return (
				<button onClick={incrementCount}>
						Count: {count}
				</button>
				<Show when={count > 5}>
						<span>Count is > 5!</span>
				</Show>
		);
}

export default SomeComponent;
```