# useState, useRef, & useEffect

> Hooks aren’t as confusing as you think
> 

---

# Intro

React hooks are a relatively new thing for React. They are simple, yet powerful. Getting used to them however can be difficult for some. This doc aims to give basic explanations and cover the normal usage of the main React hooks you will be using

# useState

In a nutshell, `state` is like a variable for the component. You can set it to whatever you want, and it helps keep track of various data. Normal variables do not persist between `re-renders` since they are redeclared every `re-render`. `state` on the other hand persists. 

```jsx
function SomeComponent() {
	// this is a local variable that stays as 'hello world' on every rerender
	let text = 'hello world';
	// this state stays the same between rerenders unless changed using the set function
	const { number, setNumber } = useState(13);
	
	return (
		<p>{text}</p>
		<p>{number}</p>
	);
}
```

You can create a `state` with `useState`. Calling `useState` returns two values. The first is a variable containing the value of the `state`, and the second is a method to set the `state` to a new value. 

```jsx
const { stateValue, setStateValue } = useState('some-string');

console.log(stateValue); // 'some-string'

setStateValue('some-other-string');
```

The main point of importance though, is that every time you change a `state`, the components that rely on that `state` are `re-rendered`. 

Note that the value of the `state` that `useState` provides does not update automatically. In fact, it only reflects the new values when the component `re-renders` and reruns the entire component’s function. In other words, calling `setState` methods does not immediately reflect changes in the current scope:

```jsx
const { stateValue, setStateValue } = useState('some-string');

console.log(stateValue); // 'some-string'

setStateValue('some-other-string');

console.log(stateValue); // still 'some-string'
// setStateValue does not immediately update stateValue
```

# useEffect

`useEffect` is the hook that lets you run code during certain steps of the component’s lifecycle. It takes a function that is run when the lifecycle requirements are met, and an optional array of `dependencies`, which are basically values that mean “only run the function code if these values change”. If any variable in the dependency array changes, then the function supplied as the first argument is run again. Not providing a dependency array causes `useEffect` to run on every `re-render`, and providing an empty dependency array (`[]`) causes `useEffect` to only run once when the component is first rendered. 

```jsx
// the following is just an example to demonstrate how useEffect behaves.
// this is actually not very good practice and should be generally avoided.
// for information on better ways to do this, refer to the React beta docs
// https://beta.reactjs.org/learn/you-might-not-need-an-effect

// For this example specifically, it would be better to console.log directly
// when count is updated, instead of having a useEffect listen in from the side.
// This results in more understandable statements that don't need to be connected
// together mentally. 

const { count, setCount } = useState(0);
const { other, setOther } = useState('irrelevant value');

// this logs whenever count changes
useEffect(() => {
	console.log(count * 2);
}, [count]); // dependency array with count

// this only logs one time, when the component is initially rendered (mounted)
useEffect(() => {
	console.log(count * 2);
}, []); // empty dependency array

// this logs whenever any state changes (essentially whenever the component 
// rerenders).
// so if "other" is updated, this would also rerun regardless 
// of whether count changed.
useEffect(() => {
	console.log(count * 2);
}); // no depedency array

// this loops infinitely because it runs on every state change, and when it runs, 
// it updates state, causing it to trigger itself again. 
useEffect(() => {
	setCount(count * 2); // setCount causes state update
}); // no depedency array
```

You can also return another function inside the `useEffect` function, which will be run when the component `unmounts`. This is particularly useful for clearing `intervals` when they’re not needed anymore to prevent memory leaks.

```jsx
const interval = useRef(); // ignore this for now, explained in next section

// this useEffect only runs once when component mounts
useEffect(() => {
	// create interval to log 'hello' every second
	// and store interval in reference
	interval.current = setInterval(() => console.log('hello'), 1000);
	
	// this code is run when the component unmounts.
	// here we just delete the interval since we don't want it anymore. 
	return () => {
		clearInterval(interval.current);
	};
}, []);
```

In addition, be careful about what dependencies you add to the array. How often do you think the useEffect will run in the example below?

```jsx
function SomeComponent() {
	const doSomethingOnMount = () => { 
		console.log('hello world');
	};
	
	// does this only run once, on mount?
	useEffect(() => {
		doSomethingOnMount();

	}, [doSomethingOnMount]);

	return (
		// ...
	);
}
```

The answer is that it will run on ********every******** rerender. `doSomethingOnMount` is redeclared on every rerender, making its object reference change on ever rerender. As a result, when React checks that the dependencies are still the same, it will find that `doSomethingOnMount` has changed, causing the `useEffect` to trigger again. Be careful of this when you add dependencies to a `useEffect` that is only supposed to run once on component mount. Ways to solve the above problem is to either declare the function outside of the component function or to use `useCallback` or `useRef` as explained in the following section. 

Another important thing to be on the lookout for is that, when developing in React strict mode (which is by default on for most if not all projects), React mounts components *****twice***** every time, causing useEffect to run two times at a minimum. This behavior will not happen in production, but when developing it could be a pain when stuff you want running only once executes twice. For your purposes, you can probably just ignore this, but if you really dislike this, you can reference the [beta docs on ways to counter this](https://beta.reactjs.org/learn/synchronizing-with-effects#how-to-handle-the-effect-firing-twice-in-development).

# useRef

`useRef` is almost the same as `useState`. Just like `useState`, you can think of it as a variable for the component that persists between `re-renders`. 

The main difference from `useState` however is that changing a `reference` does not trigger a `rerender`. This makes it useful for storing values that you want to persist between `re-renders`. 

When you create a new `reference`, it has a `.current` property where you can access or update the `reference` value. Note that unlike `useState`, updates are immediate. 

```jsx
const someReference = useRef();

console.log(someReference.current); // null

someReference.current = 'cheese';

console.log(someReference.current); // 'cheese'
```

You likely won’t need to use it much, but it does come in handy when you do. 

For example, it is used to store the `interval` in the `useEffect` example above. Another use is a shorter substitute for the `useCallback` hook, where you create a persistent reference for an object declared inside the component so that `useEffect` doesn’t unintentionally trigger on `re-renders`. 

```jsx
const someFunc = () => {
	console.log('hello world');
};

// this triggers on every rerender because someFunc is redeclared every rerender
// since someFunc is redeclared, its reference changes, causing useEffect
// to trigger again. 
useEffect(() => {
	someFunc();
}, [someFunc]);

const someOtherFunc = useRef(() => {
	console.log('hello world');
}).current; // note the .current here to immediately access the ref value

// this triggers only once on component mount
// since someOtherFunc is stored with a persistent reference
// that won't change between rerenders
useEffect(() => {
	someOtherFunc();
}, [someOtherFunc]);
```