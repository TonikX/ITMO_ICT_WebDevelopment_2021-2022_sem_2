<template>
	<div>
		<h3>Room Number {{number}}</h3>
		<p>Floor Number: {{floor}}</p>
		<p>Price: {{price}}</p>
		<p>Room Type: {{type}}</p>
		<a :href="'/rooms/' + number" class="btn btn-primary">More</a>
		<hr>
	</div>
</template>

<script>
export default {
	name: 'RoomRow',
	props: ['id', 'number', 'type', 'price', 'floor', 'cleaners']
}
</script>

<style>

</style>
