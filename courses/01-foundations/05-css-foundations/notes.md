# CSS Foundations

Started: 20 August 2026  
Completed:

## Intro to CSS

Assignment exercises:

https://github.com/mattxreynolds/css-exercises

### Knowledge Check

#### What is the syntax for class and ID selectors?

A class selector uses a period (`.`) followed by the class name. An ID selector uses a hash (`#`) followed by the ID name.

#### How would you apply a single rule to two different selectors?

Group the selectors in a comma-separated list and place their shared declarations in the same rule.

#### Given an element that has an id of title and a class of primary, how would you use both attributes for a single rule?

`#title.primary`

#### What does the descendant combinator do?

It selects elements that match the last selector when they have an ancestor that matches the preceding selector.

#### What are the names of the three ways to add CSS to HTML?

External, internal, and inline CSS.

#### What are the main differences between the three ways of adding CSS to HTML?

External CSS is written in a separate file, linked with a void `<link>` element inside the `<head>`, and can be reused across pages.

Internal CSS is written inside a `<style>` element within the `<head>` and applies only to that page.

Inline CSS is written in an element’s `style` attribute. It does not use a selector, affects only that element, and overrides external and internal CSS when their declarations conflict.

## The Cascade

### Knowledge Check

#### Between a rule that uses one class selector and a rule that uses three type selectors, which rule has the higher specificity?

The rule with one class selector.

## Inspecting HTML and CSS

### Personal Knowledge Check

#### You spot a button on a page that looks wrong. How would you open DevTools with that button selected, and where would you find its HTML and CSS?

Right-click the button and choose Inspect. Its HTML appears in the Elements panel, and its CSS appears in the Styles panel.

#### If you’ve already opened DevTools but cannot find an element in the HTML tree, how could you select it directly from the page?

Click the element-select icon in the top-left corner of DevTools, then click the element on the page.

#### You see a CSS declaration crossed out in the Styles panel. What does that tell you, and how would you investigate which style is taking effect?

The declaration is overridden by another style. Look through the Styles panel to find where that property is set.

#### You want to try a different background colour without editing your project files. What would you do in DevTools, and what would happen to that change if you reloaded the page?

Add a CSS declaration for the element in the Styles panel. The change reverts when the page reloads.

#### How could you temporarily change an element’s text or an attribute in the Elements panel? Would that change the HTML file in your editor?

Double-click the text or attribute you want to change. This does not change the HTML file in the editor.

## The Box Model

### Personal Knowledge Check

#### Describe the four layers of the CSS box model, working from the inside out.

Content contains the element’s content. Padding creates space between the content and the border. The border sits between the padding and the margin. Margin creates space outside the border, between adjacent boxes.

#### A card’s text is too close to its border, and the card is too close to its neighbour. Which property would you adjust for each problem, and why?

Adjust padding to increase the space between the text and the border. Adjust margin to increase the space between the card and its neighbour.

#### A block box has `width: 240px`, `padding: 16px`, and `border: 2px solid`. What is its total width, excluding margins, with `box-sizing: content-box`? What changes with `border-box`?

With `content-box`, the total width is 276px. With `border-box`, the total width becomes 240px.

#### What does `margin: 12px 24px 8px` set on each side?

12px on the top, 24px on the left and right, and 8px on the bottom.

#### Two vertically stacked blocks in normal flow have adjoining margins of `28px` and `16px`. If those margins collapse, what gap results, and why?

The gap is 28px because the larger margin is used.

#### How would you horizontally centre a block that is narrower than its container using margins? Would the same approach vertically centre it in normal flow?

Use `margin: auto`. This centres the block horizontally but does not centre it vertically in normal flow.

## Block and Inline
