<template>
<div>
<div>
List of workers of the farm. There you can also create a new one or edit workers' info.
</div>
<v-col>
<v-btn color="primary" dark @click='$router.push("/workerslist1")'>Workers List</v-btn>
</v-col>
<div>
List of breeds of chickens in the farm. There you can also create a new one or edit info about an existing breed.
</div>
<v-col>
<v-btn color="primary" dark @click='$router.push("/breedslist1")'>Breeds List</v-btn>
</v-col>
<div>
List of cages in the farm. There you can also create a new one or edit info about an existing cage.
</div>
<v-col>
<v-btn color="primary" dark @click='$router.push("/cageslist1")'>Cages List</v-btn>
</v-col>
<div>
List of chickens in the farm. There you can also create a new one or edit info about an existing chicken.
</div>
<v-col>
<v-btn color="primary" dark @click='$router.push("/chickenslist1")'>Chickens List</v-btn>
</v-col>
<div>
List of tasks for workers in the farm. There you can also create a new task or edit info about an existing task.
</div>
<v-col>
<v-btn color="primary" dark @click='$router.push("/taskslist1")'>Tasks List</v-btn>
</v-col>
</div>
</template>

<script>
export default {
  name: 'Home'
}
</script>
