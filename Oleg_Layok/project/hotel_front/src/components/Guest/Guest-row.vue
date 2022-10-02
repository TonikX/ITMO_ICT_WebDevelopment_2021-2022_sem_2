<template>
	<div>
		<h3>{{name}}</h3>
		<p>Passport: {{passport_number}}</p>
		<p>From Location: {{from_location}}</p>
		<a :href="'/guests/' + id" class="btn btn-primary">More</a>
		<hr>
	</div>
</template>

<script>
export default {
	name: 'GuestRow',
	props: ['id', 'passport_number', 'name', 'surname', 'middlename', 'from_location', 'check_in_date', 'check_out_date', 'prev_check_out_date', 'room']
}
</script>

<style>

</style>
