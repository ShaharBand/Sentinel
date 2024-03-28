export interface NavLinkProps {
  to: string;
  icon: React.ReactElement;
  label: string;
  selected: boolean;
  onClick?: () => void; 
}