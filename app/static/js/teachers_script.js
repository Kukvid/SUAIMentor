async function main(){
    let peopleList = await getResponse()
    const teacher_list = document.querySelector('.teachers__list')
    // let countPeople = 0;
    let countPeopleGroup = 0;
    let newRow = ""
    let groupIDs = []
    let currentPerson;
    for (let i = 0; i < peopleList.length; i+=3){
        if (i + 3 > peopleList.length) {
            if (i + 2 == peopleList.length) {
                groupIDs = [i, i + 1]
            } else if (i + 1 == peopleList.length) {
                groupIDs = [i]
            }
        }
        else{
            groupIDs = [i, i+ 1, i+2]
        }

        if ((countPeopleGroup) % 2 == 0){
            newRow = `<ul class="row row__blue">`
        }
        else{
            newRow = `<ul class="row row__grey">`
        }
        for (let peopleID of groupIDs){
           currentPerson = peopleList[peopleID]
           newRow += `
            <li class="card__teacher">
            <a class="teacher__link" href="teachers\\${peopleID}">
                <img class="teacher__image" src="../static/teachers_images/Default.png" alt="Default teacher image">
                <div class="teacher__name">
                <p class="Ubuntu-text-700-teachers">
                    ${currentPerson.last_name +" "+ currentPerson.first_name +" "+ currentPerson.middle_name}
                </p>
                </div>
                <div class="teacher__department">
                <p class="Ubuntu-text-400">
                    Кафедра ${currentPerson.department}
                </p>
                </div>
            </a>
            </li>
           `
        }
        newRow += "</ul>"
        teacher_list.innerHTML += newRow
        newRow = ""
        countPeopleGroup += 1
    }
    // console.log(peopleList)
}
// const teacher_list = document.querySelector('.teachers__list')
// console.log(teacher_list.innerHTML())

main()