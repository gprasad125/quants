# Component Lifecycle

> How React does things
> 

---

# Intro

This doc focuses on giving a better idea on how React displays, updates, and removes components so you can take better advantage of lifecycle hooks. 

# Rendering

Writing components in React is all fun and good, but how exactly does React display them? Well, components are simply `functions` that return `JSX` (HTML-like JS syntax). When React wants to `render` or display a component, it simply needs to call it like a normal function and `render` the returned `JSX`. 

What if a state changes however? How would `React` update the display? Well, then it just simply needs to recall the `component`'s function, get the new `JSX`, and display that instead. There’s a lot of simplification here of course, but `React` essentially recalls the `component` function whenever it knows something to changes, or more specifically, whenever a `state` changes. 

As a side note, this is also the reason why you cannot use methods that should only be called once, like `setInterval` , in the body of the component without wrapping it in a `useEffect`. It would simply be repeatedly called over and over again as the component re-renders. 

A useful tip is to add `console.log('some render message')` to the body of components when you want to track renders. Whenever the components render or re-render, they’ll log the message to the browser console.

# Lifecycle

Specific steps in the life of a component are outlined below

### Component mount

This is when the component is rendered or added to the display for the first time.

### Component update

This is when `state` changes causes the component to be re-rendered and become updated with the new `state` information. 

### Component unmount

This is when the component is removed from the display and dismantled.