<template>
	<div>
		<h3>Room: {{room}}</h3>
		<p>Staff: {{staff}}</p>
		<p>Cleaning Date: {{date_time}}</p>
		<a :href="'/cleanings/' + id" class="btn btn-primary">More</a>
		<hr>
	</div>
</template>

<script>

export default {
	name: 'CleaningRow',
	props: ['id', 'room', 'staff', 'date_time']
}
</script>

<style>

</style>
