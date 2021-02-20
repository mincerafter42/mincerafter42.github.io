---
title: Triangle solver
date: 2021-02-18 16:00:14 -0800
---
Say you're me and you're in math class. Yes this is a Vi (Hart) reference, but I actually have a math class. And the math class is boring.

Today in math class we did a bunch of stuff with triangles. Oh gosh it's a triangle but you don't have all the angles and sides can you find them? Yeah that was boring so I spent the afternoon making a triangle solver:
## Solve triangles and stuff
This was cool to program, definitely more interesting than having to do this logic and math for many triangles myself, but also it's very prone to floating-point-number weirdness that comes with Javascript and all the stuff with sines and cosines and Pi we gotta do (yes Javascript uses radians so Pi is needed)  
It doesn't make sure the angles add up to 180° like they should because that just kept producing false negatives.

![A triangle with corners labeled with the uppercase letters A, B, C, and their opposing edges labeled with the lowercase letters a, b, c]({{ "/assets/triangle.png" | absolute_url }})

<label>Angle A (degrees) <input type="number" min="0" max="180" step="any" id="A" /></label>  
<label>Angle B (degrees) <input type="number" min="0" max="180" step="any" id="B" /></label>  
<label>Angle C (degrees) <input type="number" min="0" max="180" step="any" id="C" /></label>

<label>Edge a <input type="number" min="0" step="any" id="a" /></label>  
<label>Edge b <input type="number" min="0" step="any" id="b" /></label>  
<label>Edge c <input type="number" min="0" step="any" id="c" /></label>

<button type="button" id="solve">Solve Triangle</button>
<div id="solved"></div>
<script>
const degrees = Math.PI/180; // need this to convert angles between degrees and radians
function solveTriangle(A,B,C,a,b,c) { // given a triangle with angles A, B, C (degrees) and edges a, b, c, solves for any missing values
	const knownEdgeCount = (!isNaN(a))+(!isNaN(b))+(!isNaN(c)), knownAngleCount = (!isNaN(A))+(!isNaN(B))+(!isNaN(C)); // count known edges and angles
	console.log(knownEdgeCount);
	console.log(knownAngleCount);
	if (knownEdgeCount==0) return "Triangle cannot be solved with 0 edges";
	switch (knownAngleCount) {
		case 0:
			if (knownEdgeCount==3) B = Math.acos((b*b-c*c-a*a)/(-2*a*c))/degrees; // find one angle if all edges are known
			else return "Not enough angles to solve";
		case 1:
			if (knownEdgeCount==1) return "Not enough angles to solve";
			[a,b,c] = [a||Math.sqrt(b*b+c*c-2*c*b*Math.cos(A*degrees)),b||Math.sqrt(c*c+a*a-2*a*c*Math.cos(B*degrees)),c||Math.sqrt(a*a+b*b-2*a*b*Math.cos(C*degrees))]; // for case where the known angle isn't opposite to an edge
			const common = (Math.sin(A*degrees)/a)||(Math.sin(B*degrees)/b)||(Math.sin(C*degrees)/c); // use sine law to find 1 or 2 more angles
			[A,B,C] = [A||(Math.asin(a*common)/degrees), B||(Math.asin(b*common)/degrees), C||(Math.asin(c*common)/degrees)];
		case 2:
			const finalAngle = 180-(A||0)-(B||0)-(C||0); // angles in a triangle always add up to 180 degrees
			[A,B,C] = [A||finalAngle, B||finalAngle, C||finalAngle];
	}
	console.log([A,B,C])
	if (A>0&&B>0&&C>0) { // sanity check for angles
		// find edges (using sine law)
		const common = (a/Math.sin(A*degrees))||(b/Math.sin(B*degrees))||(c/Math.sin(C*degrees));
		[a,b,c] = [a||(common*Math.sin(A*degrees)), b||(common*Math.sin(B*degrees)), c||(common*Math.sin(C*degrees))];
		console.log([a,b,c])
		if (a>0 && b>0 && c>0 && a<b+c && b<a+c && c<a+b) return [A,B,C,a,b,c]; // sanity check for edges, return triangle if fine
		else return "Invalid edges"
	}
	else return "Invalid angles";
}
document.getElementById("solve").addEventListener("click", ()=>{
	const solved = solveTriangle(
	Number(document.getElementById("A").value||NaN),
	Number(document.getElementById("B").value||NaN),
	Number(document.getElementById("C").value||NaN),
	Number(document.getElementById("a").value||NaN),
	Number(document.getElementById("b").value||NaN),
	Number(document.getElementById("c").value||NaN));
	if (typeof solved === "object") document.getElementById("solved").innerHTML = "Angle A (degrees): "+solved[0]+"<br />Angle B (degrees): "+solved[1]+"<br />Angle C (degrees): "+solved[2]+"<br /><br />Edge a: "+solved[3]+"<br />Edge b: "+solved[4]+"<br />Edge c: "+solved[5];
	else document.getElementById("solved").innerText = solved;
});
</script>

Sorry I haven't been posting for a while, not sure why. I want to do cool stuff and share cool stuff here. Maybe the new semester is giving me more work to do and less time to do cool stuff. School is weird.
