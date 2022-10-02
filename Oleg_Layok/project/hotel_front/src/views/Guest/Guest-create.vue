<template>
	<guest-form
		:mode="'add'"
	/>
</template>

<script>
import GuestForm from '../../components/Guest/Guest-form.vue'

export default {
	components: { GuestForm },
	name: 'GuestCreate'
}
</script>

<style>

</style>
