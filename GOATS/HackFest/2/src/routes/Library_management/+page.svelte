<script>
    class student{
        /**
         * @param {any} name
         * @param {any} rollno
         */
        constructor(name,rollno){
            this.name=name;
            this.rollno=rollno;
            /**
             * @type {any[]}
             */
            this.books=[];
            this.fine=0;
        }
        getfine(){
        }
    }
    class books{
        /**
         * @param {String} bookname
         * @param {any} id
         */
        constructor(bookname,id){
            this.bookname=bookname;
            this.id=id;
            this.Issuedate = new Date();
            this.Duedate = new Date();
        }
    }
    let name='';
    let roll='';
    let bookname='';
    let id='';
    let std = [new student("mandar","10000"),new student("sagar","10001"),new student("sanket","10002"),new student("saurabh","10003"),new student("siddhesh","10004"),new student("siddhant","10005"),new student("siddharth","10006"),new student("siddhesh","10007")];
    function addstudent(){
        let x =new student(name,roll);
        std = [...std,x];
        name='';
        roll='';
    
    }
    function Issuebook(){;
        bt.Issuedate=(_date)
        let a =new Date().getTime() 
        let b = new Date(_date).getTime()
        let c = new Date(b+7*24*60*60*1000);
        let diffDays = Math.floor(((a-b)/(1000*3600*24) -7));
        bt.fine= diffDays>0?(diffDays)*10:0;
        bt.Duedate= c;
        st.books=[...st.books,bt]
        st.fine=st.books.reduce((a,b)=>a+b.fine,0);
        std=[...std];
        bt='';
    }
    let bk = [new books("maths","1"),new books("science","2"),new books("english","3"),new books("hindi","4"),new books("computer","5")];
    
    function addbook(){
        bk =[...bk,new books(bookname,id)];
        bookname = '';
        id = '';
    }
    /**
     * @type {student}
     */
    let st;
    /**
     * @type {any}
     */
    let bt;
    /**
     * @type {Date}
     */
    let _date;
</script>
<main class="text-xl bg-stone-200 h-max grid place-items-center p-4  pt- 16 shadow-3xl">
    <p Class ="bg-opacity-60 bg-teal-400 rounded-2xl p-3 text-5xl m-6 text-thin "><u>Add Student</u></p>
<div class="shadow-2xl w-4/5  grid place-items-center h-max p-6"> 
    <div class="px-32 py-6 bg-teal-400 h-max rounded-3xl shadow-2xl m-8">
    <!-- svelte-ignore a11y-label-has-associated-control -->
    <label>name</label>
    <input type="text" class="b-1" bind:value={name}>
    <!-- svelte-ignore a11y-label-has-associated-control -->
    <label>rollno</label>
    <input type="text" bind:value={roll}>
    <button on:click={addstudent}>submit</button>
    </div>

    <table class="m-1 p-1 w-4/5 shadow-2xl">
        <tr class="border-4 border-black w-4/5 bg-blue-200 ">
            <th class="p-4 border-2 border-black w-10">Name</th>
            <th class="p-4 border-2 border-black">Roll</th>
            <th class="p-4 border-2 border-black">Fine</th>
            <th class="p-4 border-2 border-black">books</th>

        </tr>
        {#each std as mb}
        <tr class="border-4 w-4/5 shadow-2xl">
            <td class="px-4 py-2 border-2 border-black ">{mb.name}</td>
            <td class="px-4 py-2 border-2 border-black">{mb.rollno}</td>
            <td class="px-4 py-2 border-2 border-black">{mb.fine}</td>
            <td class="px-4 py-2 border-2 border-black">{mb.books.length}</td>
        </tr>
        {/each}
 </div>

 <p Class ="bg-opacity-60 bg-teal-400 m-6 rounded-2xl p-3 text-5xl text-thin "><u>Add Books</u></p>

<div class="shadow-2xl w-4/5 h-max p-6 grid place-items-center"> 
    <div class="grid place-items- w-4/5 px-32 py-6 bg-teal-400 max rounded-3xl shadow-2xl m-8">
    <!-- svelte-ignore a11y-label-has-associated-control -->
    <label>bookname</label>
    <input type="text" bind:value={bookname}>
    <!-- svelte-ignore a11y-label-has-associated-control -->
    <label>id</label>
    <input type="text" bind:value={id}>
    <button on:click={addbook}>submit</button></div>
    <table class="m-1 p-1 w-4/5 shadow-2xl">
        <tr class="border-4 border-black w-4/5 bg-blue-200">
            <th class="p-4 border-2 border-black ">Name</th>
            <th class="p-4 border-2 border-black w-1/3">Id</th>
        </tr>
        {#each bk as mb}
        <tr class="border-4 w-4/5 shadow-2xl">
            <td class="px-4 py-2 border-2 border-black ">{mb.bookname}</td>
            <td class="px-4 py-2 border-2 border-black w-10">{mb.id}</td>
        </tr>
        {/each}
</div>

 
<p Class ="bg-opacity-60 bg-teal-400  rounded-2xl p-3 m-6 text-5xl text-thin "><u>Issue Books</u></p>
    
  <div class="shadow-2xl w-4/5 h-max py-3 px-56">
    
    <lable>student name</lable>
    <select bind:value={st}  class="flex  justify-between-between">
        {#each std as s}
        <option value={s}>{s.name}</option>
        {/each}
        </select>
    <lable>book name</lable>
    <select bind:value={bt}>
        {#each bk as b}
        <option value={b}>{b.bookname}</option>
        {/each}
        </select>
    <lable>Issue date</lable>
        <input bind:value={_date}  type="date"/>

    
    
    
<div/>
<div class="grid w-full">
<lable>student name</lable>
<select bind:value={st} >
    {#each std as s}
    <option value={s}>{s.name}</option>
    {/each}
</select>
<button on:click={Issuebook}>submit</button>
        {#if st}
        <table class="m-1 p-1 shadow-2xl ">
            <tr class="border-4 border-black bg-blue-200 w-4/5">
                <th class="p-4 border-2 border-black w-10">Name</th>
                <th class="p-4 border-2 border-black">Id</th>
                <th class="p-4 border-2 border-black">Issue date</th>
                <th class="p-4 border-2 border-black">due date</th>
                <th class="p-4 border-2 border-black">fine</th>
                <th class="p-4 border-2 border-black">Return</th>
            </tr>
            {#each st.books as mb}
            <tr class="border-4 w-4/5 shadow-2xl">
                <td class="px-4 py-2 border-2 border-black w-10">{mb.bookname}</td>
                <td class="px-4 py-2 border-2 border-black">{mb.id}</td>
                <td class="px-4 py-2 border-2 border-black">{mb.Issuedate}</td>
                <td class="px-4 py-2 border-2 border-black">{mb.Duedate.toString()}</td>
                <td class="px-4 py-2 border-2 border-black">{mb.fine}</td>
                <td class="px-4 py-2 border-2 border-black"><button on:click={()=>{st.books=st.books.filter(m => m!=mb)}}>Return</button></td>
            </tr>
            {/each}
        </table>
        {/if}
</div>
</main>

<!-- done -->