import React, { useState } from "react";
import Select from "react-select";

const options = [
    { value: "who", label: "Visitors of the Park", id: 0 },
    { value: "how-often", label: "Frequency of Visits", id: 1 },
    { value: "safety", label: "Park Safety and Maintainence Ratings", id: 2 },
    {
        value: "safety-over-time",
        label: "Safety and Maintainenece Trends Over Time",
        id: 3,
    },
    { value: "exist", label: "Locals' Knowledge of CPC Existence", id: 4 },
    { value: "why", label: "Reasons For Visiting CPC", id: 5 },
    { value: "services-yn", label: "Need For Services in the Park", id: 6 },
    { value: "services-types", label: "Types of Services Desired", id: 7 },
];

const Dropdown = () => {
    const [selectedOption, setSelectedOption] = useState(0);
    const [id, setId] = useState(0);

    const handleOptionChange = (selectedOption) => {
        setSelectedOption(selectedOption);
        console.log(selectedOption.id);
        setId(selectedOption.id);
    };

    const PAGES = [
        {
            component: <h1> insert 1 here</h1>,
        },
        {
            component: <h1> insert 2 here</h1>,
        },
        {
            component: <h1> insert 3 here</h1>,
        },
        {
            component: <h1> insert 4 here</h1>,
        },
        {
            component: <h1> insert 5 here</h1>,
        },
        {
            component: <h1> insert 6 here</h1>,
        },
        {
            component: <h1> insert 7 here</h1>,
        },
        {
            component: <h1> insert 8 here</h1>,
        },
    ];

    return (
        <div>
            <Select
                options={options}
                value={selectedOption}
                onChange={handleOptionChange}
            />
            <h2> {PAGES[id].component} </h2>
        </div>
    );
};

export default Dropdown;
