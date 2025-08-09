import AutocompleteInput from '../AutocompleteInput';
import { buildSearchFn, buildDetailFn, getCustomerSearchPath } from '../../api/autocompleteApi';

export default function CustomerAutocomplete({
                                                 value,
                                                 onSelect,
                                                 error,
                                                 displayField,
                                                 onCreateNewClick,
                                                 required,
                                                 placeholder = "Search customer...",
                                                 ...props
                                             }) {
    return (
        <div>
            <label className="block font-medium mb-1 capitalize">
                Customer
                {required && <span className="text-red-500 ml-1">*</span>}
            </label>

            <AutocompleteInput
                value={value}
                onSelect={onSelect}
                searchFn={buildSearchFn(getCustomerSearchPath)}
                getDetailFn={buildDetailFn('customers/api/customers')}
                displayField={displayField}
                onCreateNewClick={onCreateNewClick}
                placeholder={placeholder}
                error={error}
                {...props}
            />
        </div>
    );
}
